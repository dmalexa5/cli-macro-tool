import messages
from sys import exit
import route
from re import match

def main():
    
    print(messages.HEADER, messages.INTRO)

    while True:
        
        user_input = input(messages.CLI)
        
        if user_input in ['exit', 'quit', 'q', 'stop']:
            print(messages.EXIT)
            exit()

        command, flag, args = parse(user_input)

        if flag == None or command == None:
            print(args)
            continue
        
        if command == 'part':
            part(flag, args)

        elif command == 'weldment':
            weldment(flag, args)

def part(flag:str, args:str):

    records = [] # list to store the records for this part

    flag = flag[1:] # remove '-'

    # Get usages
    for index, key in enumerate(flag):

        record = PART_RECORDS[key] # Get record

        new_record = [str((index+1)*10)] + record # Insert sequence

        usage = args[index] if args != None \
            else get_usage(new_record[2], new_record[1]) # Get usage

        new_record.insert(3, usage) # Insert usage

        records.append(new_record)

    start_macro(records) # Execute part macro
    return 

def weldment(flag:str, args:str):

    records = [] # list to store the records for this weldment

    flag = flag[1:] # remove '-'

    painted = 2 if flag[-1] == 'P' else 1 # determine if painted or not

    for i in range(0, painted):
        
        if flag[-1] == 'P':
            record = WELDMENT_RECORDS[flag[:-1] if i == 0 else 'P']
        else:
            record = WELDMENT_RECORDS[flag if i == 0 else 'P']

        new_record = [str((i + 1) * 10)] + record # Insert sequence

        # Insert usage
        if args == None:
            new_record.insert(3, get_usage(new_record[2], new_record[1]))

        else:
            new_record.insert(3, args[i])

        records.append(new_record)
    
    start_macro(records) # Execute weldment macro   
    return

def get_usage(resource, cell):

    while True:
        usage = input(f"Enter {resource} usage for cell {cell}: ")

        try:
            usage = str(round(float(usage), 2))

        except Exception:
            print(messages.ERROR_NAN_USAGE(usage))
            continue
            
        return usage

def get_part_number() -> str:

    while True:
        pn = input(f"Enter part number: ")

        if len(pn) == 9 and pn.isdigit():
            return pn
            
        else:
            print(messages.ERROR_INVALID_PART_NUMBER)

def get_locator() -> str:
    
    while True:
        locator = input(f"Enter locator: ")

        # Must follow the pattern dd-dd or dd-CUSTOM
        pattern = r'^\d{2}-\d{2}$|^\d{2}-CUSTOM$'

        if match(pattern, locator):
            return locator
            
        else:
            print(messages.ERROR_INVALID_LOCATOR)

def start_macro(records:list):

    macro = route.Macro(records) # Initialize macro

    
    pn = get_part_number()
    locator = get_locator()

    # Routings Macro
    listener = route.Listener(lambda: macro.route_part(pn))  
    print("\nCtrl + Shift + Click in the Oracle routings item box...")
    listener.run()
    
    # Locator PN Macro / pre-locator prep macro
    listener = route.Listener(lambda: macro.enter_locator_pn(pn))
    print("\nCtrl + Shift + Click in the Zoom -> Item Number box...\n")
    listener.run()

    # Locator Macro
    listener = route.Listener(lambda: macro.enter_locator(locator))
    print("\nCtrl + Shift + Click in the POU locator box...\n")
    listener.run()

    print("\n\nComplete.")
    return

def parse(input:str):

    # Pre-processing
    input = input.split(' ')
    input = [_ for _ in input if _ != ''] # remove spaces

    # Check command
    command = input[0]
    
    if command == 'help':
        return None, None, messages.HELP

    elif command not in ['part', 'weldment']:
        return None, None, messages.ERROR_UNRECOGNIZED_COMMAND(command)
    
    # Check if more than one command entered
    if len(input) == 1:
        return None, None, messages.ERROR_MISSING_FLAG

    if input[1][0] != '-':
        return None, None, messages.ERROR_UNRECOGNIZED_COMMAND(input[1])
    
    # Find flag
    flags = [_ for _ in input[1:] if _[0] == '-']

    if len(flags) == 0:
        return None, None, messages.ERROR_MISSING_FLAG
    
    elif len(flags) > 1:
        return None, None, messages.ERROR_MULTIPLE_FLAGS
    
    flag = flags[0]

    # Check flag
    if (command == 'part' and flag not in VALID_PART_FLAGS) or \
        (command == 'weldment' and flag not in VALID_WELDMENT_FLAGS):

        return None, None, messages.ERROR_INVALID_FLAG

    # Check usages and round to 2 digits
    args = input[2:]

    for usage in args:

        try:
            usage = str(round(float(usage), 2))
        except:
            return None, None, messages.ERROR_NAN_USAGE(usage)

    # Check the number of usages
    if len(args) == 0:
        return command, flag, None
    
    if command == 'weldment':
        if flag[-1] == 'P' and len(args) != 2:
            return None, None, messages.ERROR_USAGES(len(args), 2)
        
        elif flag[-1] != 'P' and len(args) != 1:
            return None, None, messages.ERROR_USAGES(len(args), 1)

    if command == 'part' and len(args) != len(flag) - 1:
        return None, None, messages.ERROR_USAGES(len(args), 2)
    
    return command, flag, args

VALID_PART_FLAGS = [
    '-l',
    '-le', # Flat piece part
    '-leb', # Standard piece part
    '-leB', # Large piece part
    '-lebp',
    '-leBp',
    '-lep',
    '-s',
    '-sb',
    '-sB', # Not sure if this one is actually allowed
    
    # All drilled parts
    '-ld',
    '-led', # Flat piece part
    '-lebd', # Standard piece part
    '-leBd', # Large piece part
    '-lebdp',
    '-leBdp',
    '-sd',

    # Edge cases where welding tabs is required
    '-lebw', # Standard piece part
    '-leBw', # Large piece part
    '-lebwp',
    '-leBwp',
]

VALID_WELDMENT_FLAGS = [
    '-mp',
    '-mb',
    '-sub', # Subbases
    '-mpP',
    '-mbP',
    '-subP'
]

# All current supported part records
PART_RECORDS = {
    'l': ['250001', 'MACHINIST', 'LASER CUT PART'],
    'e': ['EDGEGRIND', 'MACH OPER', 'GRIND EDGES'],
    'b': ['101001', 'MACHINIST', 'FORM BENDS'],
    'B': ['LRG BRAKE', 'MACH OPER', 'FORM BENDS'],
    's': ['104001', 'MACH OPER', 'CUT TO LENGTH'],
    'd': ['109001', 'MACH OPER', 'DRILL TO PRINT'],
    'p': ['095424', 'PAINTER', 'POWDER PAINT PART'],
}

# All current supported part records
WELDMENT_RECORDS = {
    'mb': ['MED BENT', 'WELDER', 'ASSEMBLE AND WELD'],
    'mp': ['400001', 'WELDER', 'ASSEMBLE AND WELD'],
    'sub': ['465001', 'WELDER', 'ASSEMBLE AND WELD'],
    'P': ['095424', 'PAINTER', 'POWDER PAINT WELDMENT']
}


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
    