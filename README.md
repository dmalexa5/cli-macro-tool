[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT HEADER -->
<br />
<div align="center">
    <img src="images/screenshot.png" alt="Logo" width="700" height="300">
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Before this project, each individual routing could over upwards of 12 minutes for a new engineer, and around 5 to 6 minutes for a more experienced engineer who has accumulated the necessary tribal knowledge.

**Now, it takes 50 seconds for an experienced engineer and under 3 minutes for someone new.**


What's different:
* Instead of collecting usages, cell codes, and locators from 3 different spreadsheets, everything is compiled into `Plant 24 Routing Calculator`. (Not included in this repo)
* Usages can be entered in one line, instead of wasting time clicking around different oracle apps.

Not all routings can be entered with this tool. The vast majority, however, are simple piece parts and weldments that can (and should) be routed and located blazingly fast.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation

_For co-ops/interns: It is recommended that you download and run `dist/main.exe`. However, if you do want to edit and/or build the source code:_

1. Clone the repo
   ```sh
   git clone https://github.com/dmalexa5/cli-macro-tool
   ```
2. In `cli-macro-project`, build using`pyinstaller` or run directly

   ```sh
   pyinstaller -F main.py
   ```
   or
   ```sh
   python main.py
   ```
If you built using pyinstaller, run `cli-macro-project\dist\main.exe`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

```txt
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
```

Say you are routing a standard piece part through the fabrication shop: (_Note: most of the information on this drawing is proprietary and has been erased._)

<a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/example.png" alt="Engineering drawing" width="700" height="450">
</a>

<br>

### Enter the circled information into the `Plant 24 Routing Calculator`

- In this case, there should be 2 usages: 1 for lasers and 1 for edgegrind

### Next, enter the part command with lasers + edgegrind flags: `part -le`

Follow the prompts:
```
 >> part -le
Enter MACHINIST usage for cell 250001: 0.1              Example usage
Enter MACH OPER usage for cell EDGEGRIND: 0.1           Example usage
Enter part number: 123456789                            Example 9-digit PN
Enter locator: 00-00                                    Example locator

Ctrl + Shift + Click in the Oracle routings item box...

```
Find the oracle routings item box, and press Ctrl + Shift + Click to activate the first third of the macro. After you click, hands off your keyboard and mouse!

You should see the following output in the command window, and (if done correctly) a full routing will automatically be entered into oracle.

```
Running macro...
10  250001  MACHINIST  0.1  LASER CUT PART
20  EDGEGRIND  MACH OPER  0.1  GRIND EDGES

Ctrl + Shift + Click in the Zoom -> Item Number box...
```
Next, Ctrl + Shift + Click in the Item Number box after clicking the zoom function.
```
Running macro...

Ctrl + Shift + Click in the POU locator box...

```
Finally, Ctrl + Shift + Click in the POU box.
```
Running macro...


Complete.

    >> 
```

Congratulations!! You've (hopefully) successfully entered a part routing into the fabrication system. I'd recommend manually checking this first one to make sure everything is right.

Weldments are the same. Getting the usages is slightly more difficult.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Although this tool is very specific to one use case, any contributions you make are greatly appreciated! (Hint: future interns and co-ops...)

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

David Alexander - [@dmalexa5](https://github.com/dmalexa5/)

Project Link - [https://github.com/dmalexa5/cli-macro-tool](https://github.com/dmalexa5/cli-macro-tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

README template used from: [https://github.com/othneildrew/Best-README-Template/tree/main](https://github.com/othneildrew/Best-README-Template/tree/main)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/dmalexa5/cli-macro-tool/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dmalexa5/
