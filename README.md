<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Portfolio][moreinfo-shield]][moreinfo-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Metropolis-Hastings MCMC Inference of a 3D Line</h3>

  <p align="center">
    A demonstration of the Metropolis-Hastings MCMC algorithm that infers the parameters of a 3D line from noisy 2D images taken by perspective cameras and using their projection (<i>u,v</i>) plane.
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project uses the Metropolis-Hastings Markov Chain Monte Carlo (MCMC) algorithm to infer the parameters of a given 3D line through the use of one and two perspective cameras' projection (u,v) plane. The images captured by the cameras contain noise, modeled as Gaussian, which is added to each point on the line.

In this problem, from the noisy images captured by the cameras, sample points are extracted from the images at different intervals, and these points serve as inputs to the Metropolis-Hastings algorithm.

The algorithm begins by generating initial point proposals by sampling them from a given prior distribution, and then iteratively samples new points based on the camera images and extracted sample points. Metropolis-Hastings algorithm in theory will always converge on a distribution, which is why it is being used to infer the parameters of the 3D line from the noisy images.

Initially, the result of the 3D line's parameters inferred from using one camera only manages to properly converge on two of the line's axes, which makes sense as it is hard to infer the depth axis of the line's points from a 2D noisy image taken by one perspective camera.

To solve this problem and to help the algorithm converge on the line's parameters faster, a second camera with a different position is used. Metropolis-Hastings is then run again but now with the input of both cameras, and finally, you can see in the result that all three axes of the 3D line were converged upon and that time of convergence was quicker than with only the use of one camera.

**Note**: _In order to view the project's objective, you can read [ista421ML-f2021-final-project-OptionA-MCMC.pdf](./ista421ML-f2021-final-project-OptionA-MCMC.pdf). If you want to see the output alongside the conclusions drawn from the project, you can read [final_project_OptionA_answers.pdf](./final_project_OptionA_answers.pdf)._

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

The project uses the following dependencies. It is necessary to install them before running the script.

* numpy
  ```sh
  pip install numpy
  ```
* scipy
  ```sh
  pip install scipy
  ```
* matplotlib
  ```sh
  pip install matplotlib
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/empobla/Inference-of-a-3D-Line.git
   ```
2. Enter the code directory
   ```sh
   cd code
   ```
3. Run the script
   ```sh
   python index.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

When running `index.py`, you will notice that initially your console seems to be doing nothing. This is normal, as it is running the Metropolis-Hastings algorithm's first 10% of samples (out of 50,000 total samples) for the first camera. This is a slow process, so just have patience. You will see progress updates in the console as follows:

```sh
M-H is 0.1 done
M-H is 0.2 done
M-H is 0.3 done
M-H is 0.4 done
M-H is 0.5 done
M-H is 0.6 done
M-H is 0.7 done
M-H is 0.8 done
M-H is 0.9 done
```

Once these samples are done, the script will show you plots with the approximated 3D line. In addition, these plots will be saved automatically under the `figures/` directory.

|  |  |  |
|------------|-------------|-------------|
| <img src='figures/accepted_pi.png' width='100%'> | <img src='figures/accepted_pf.png' width='100%'> | <img src='figures/map_cam1.png' width='100%'>

After showing the plots, the script will proceed to run the Metropolis-Hastings algorithm taking into account two cameras instead of one. This, as the previous process, is also a slow process. The script will show you it's progress in the console as follows:

```sh
M-H T5 is 0.1 done
M-H T5 is 0.2 done
M-H T5 is 0.3 done
M-H T5 is 0.4 done
M-H T5 is 0.5 done
M-H T5 is 0.6 done
M-H T5 is 0.7 done
M-H T5 is 0.8 done
M-H T5 is 0.9 done
```

Once this is done, the script will show you new plots with the approximated 3D line. You will notice that the program managed to better approximate the 3D line in less samples due to the use of two cameras. These plots will also be saved automatically under the `figures/` directory.

|  |  |  |  |
|------------|-------------|-------------|-------------|
| <img src='figures/accepted_pi_both_cams.png' width='100%'> | <img src='figures/accepted_pf_both_cams.png' width='100%'> | <img src='figures/map_cam1_both_cams.png' width='100%'> | <img src='figures/map_cam2_both_cams.png' width='100%'>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This project is property of Emilio Popovits Blake. All rights are reserved. Modification or redistribution of this code must have _explicit_ consent from the owner.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Emilio Popovits Blake - [Contact](https://emilioppv.com/contact)

Project Link: [https://github.com/empobla/Inference-of-a-3D-Line](https://github.com/empobla/Inference-of-a-3D-Line)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/emilio-popovits

[Python]: https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffdc52
[Python-url]: https://www.python.org/

[moreinfo-url]: https://emilioppv.com/projects#metropolis-hastings-3d-line
[moreinfo-shield]: https://img.shields.io/badge/more%20info-1b1f24?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAApVBMVEUbHyQbHyQbHyRnam2sra+vsbKys7Wsrq+goqQwNDgaHyQaIilbXWGChIZMT1OYmpwYQFoaICYXRF8WUHQZLjwvMzdwcnaztLZ1d3pcX2IaICUXTG0WUHMXS2sXSGcWT3MaKjcpLTFVWFyFh4lTVllvcnWpqqwYOEwZM0QXTW4XTnAaJS8lKS3IycoYPlYaIyt4e36rra60tba5urutr7BQU1cAAAB8HBV3AAAAAnRSTlOR/KrCyFQAAAABYktHRDZHv4jRAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wEZCiUZVutNzgAAAGpJREFUCNdjYGBkggNGBmQeiM+EAjC5zCwsrGzsHJwQLhc3ExMPLxMfP5OAIBODkLCIqBi/uASHpJS0jCyDnLyCopIyh4qqmrqGphYDk5Q2WLGOrh63PsgoA0NDI2NDE1PsFqFw0RyJ6gUAuK4HVipJCoQAAAAuelRYdGRhdGU6Y3JlYXRlAAAImTMyMDLWNTDUNTINMTSwMja3MjLVNjCwMjAAAEFRBQlQZi6pAAAALnpUWHRkYXRlOm1vZGlmeQAACJkzMjAy1jUw1DUyDTE0sDI2tzIy1TYwsDIwAABBUQUJeVmGIQAAAABJRU5ErkJggg==