HEADER = """
 ______________________________________________________________________________
       ______  _____  _     _ _______ _____ __   _  ______ _______          
      |_____/ |     | |     |    |      |   | \  | |  ____ |______          
      |    \_ |_____| |_____|    |    __|__ |  \_| |_____| ______|          
                                                                            
 _______ _______ _______  ______  _____       _______  _____   _____        
 |  |  | |_____| |       |_____/ |     |         |    |     | |     | |     
 |  |  | |     | |_____  |    \_ |_____|         |    |_____| |_____| |_____
 ______________________________________________________________________________
 
 """
# https://patorjk.com/software/taag/#p=display&f=Cyberlarge&t=%20ROUTINGS%20%0AMACRO%20TOOL

INTRO = """
Enter 'help' to display commands. Enter 'exit' to quit. 'Ctrl^C' at any time to harsh exit.
"""

CLI = " >> "

HELP = """
Commands:
  part    Create a new part routing.
    -l            Lasers
    -e            Edgegrind
    -b            Small Brake
    -B            Large Brake
    -p            Paint part
    -s            Saw cut
    -d            Drill and Tap
    -w            Weld at MED BENT

    i.e. >> part -leBp
            <Runs the wizard for a large bent painted piece part>

         >> part -le 0.5 0.63
            <Skips wizard and runs the macro for a flat piece part. 
              Usages are given sequentially.>

  weldment    Delete an existing resource
    -mb            Medium Bent
    -mp            Medium Parts
    -sub           Subbases
    -P             Paint weldment

    i.e. >> weldment -mbP
            <Runs the wizard for a medium bent painted weldment>

         >> weldment -mpP 12 6
            <Skips wizard and runs the macro for a painted bent weldment. 
              Usages are given sequentially.>

  help        Display this help message

  exit        Exit program
    Aliases:
    - quit, q
    - stop
  """

def GET_USAGE(cell) -> str:
    return f"Enter resource usage for {cell}: "

EXIT = "\nExiting Routings Macro Tool.\n"

#
# Error messages
#

def ERROR_UNRECOGNIZED_COMMAND(command) -> str:
    return f"ERROR: Unrecognised command '{command}'.\n"

ERROR_MULTIPLE_FLAGS = "ERROR: Multiple flags found. Please combine into one flag."

ERROR_MISSING_FLAG = "ERROR: Flag not found."

ERROR_INVALID_FLAG = "ERROR: The provided flag is invalid.\nRoute this part by hand or enter a more common sequence."

ERROR_INVALID_PART_NUMBER = "ERROR: Part number is wrong. Must be a 9-digit long number."

ERROR_INVALID_LOCATOR = "ERROR: Invalid locator. Must follow the format xx-xx or xx-CUSTOM."

def ERROR_USAGES(num, expected) -> str:
  return f"ERROR: Found {num} usages, expected {expected}."

def ERROR_NAN_USAGE(usage:str) -> str:
   return f"ERROR: Usage '{usage}' is not a number."