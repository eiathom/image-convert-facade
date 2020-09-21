# using

since this library _uses_ `imagemagick` under the hood, the binary (executable)
program needs to be installed to use this library,
see [here](https://www.imagemagick.org/script/download.php).

alternatively, a Docker file has been created to use this library containerized
(thereby not affecting the host OS, or need to install a binary on the host).

# running

this library was built under `Python 3.6.6`

## install python environment

```sh

python3 -m venv venv

. venv/bin/activate

```

## install dependencies

```sh

make install

# if make is not installed on this system

pip install -r requirements.txt

```

## running tests

### local

```sh

make test

# if make is not installed on this system

pytest -sv lib/test/

```

### containerised

```sh

make docker-build

make docker-run-tests

# if make is not installed on this system

docker build -t image-convert-facade .

docker run -it --rm --name icf image-convert-facade bash

pytest -sv lib/test/

```

## running a version of the CLI (locally or containerised)

```sh

# cli version 1

python main.py jpeg_scaler -h  # get help

# example

python main.py jpeg_scaler -i path/to/image/file.jpg -o name_of_output_file -s number_to_scale_by

# cli version 2

python main.py jpeg_scaler_v2 -h  # get help

# example

python main.py jpeg_scaler_v2 -d path/to/json/file.json

```

# first principles

why this will present value:
- _this_ functionality provides a simple interface to an exiting one (a __facade__)
    - a facade hides complexity
        - also referred to as a _'wrapper'_
- this will be an __optimisation__ of original functionality (not innovative)
    - general users perhaps just want to either convert or resize or both
        - we are presenting this simplification as an optimisation over the
            existing API
    - the existing API has many options
        - a _"professional"_ user perhaps finds this desirable

## architecture

### layers

```txt
-------------------------------
PRESENTATION
        [cli]
        - handles client requests
-------------------------------
APPLICATION
        [service]
        - handles requests from upstream
        - thin layer
        - no business logic
        - coordinates tasks (to downstream)
-------------------------------
DOMAIN
        [model]
        - most important layer
        - defines the business case
-------------------------------
INFRASTRUCTURE
        [io]
        - issues commands on behalf of the domain
        - targets can be:
            - data-stores
            - file-system
            - network
-------------------------------
```

a __client__ of the system interacts with _'it'_ though the cli or api

the __domain__ should not depend on any other layer

each layer is __communicating__ downstream; no upstream communication should be
possible within the layered architecture

# domain model

value extracted:
- image(s) scaled

## domain

"image scaling"

- image-resizer

## model

processes which - combine to - extract value

### image-resizer

this service is presented as a __facade__ over existing functionality

what we are presenting is a simplification of the image geometry options where we
wrap:
- `convert {input_filename_with_filetype} -resize {height}{x{width}: optional} {operator: optional} {output_filename_with_filetype}`

as:
- `{scale}`
    - under the hood we apply `{scale}` to both `{height}` and `{width}` and use
    the `%` operator

to the caller

processes:
- scale an image

# cli

showing the functionality each CLI version provides (v1, v2) and, future
functionality (v3)

## version 1

- `"jpeg-scaler"`: resize a JPEG image using a scale value
    - args:
        - [0] `input_filepath`:
            - string
            - the path to the image to scale
            - if no path:
                - image is assumed to be located in the same context (location)
                    of program execution
        - [1] `scale`:
            - integer
            - the percentage scaling factor for this image
                - 50 means, image (width, height) is scaled _down_ half
                    the original size (preserving aspect ratio)
                - 100 means, no scaling
                - 150 means, image (width, height) is scaled _up_ half
                    the original size (preserving aspect ratio)
            - positive value accepted only
        - [2] `output_filename`:
            - string
            - name given for the scaled image
            - __the image will be located under the same path as the original image__

## version 2

- `"jpeg-scaler"`: resize JPEG image(s) each with a scale value
    - arg:
        - `--data`: data is a JSON object

in this version, an array of images - passed as json - can be scaled

the args, and their meaning, are the same as before

json format:
```json
{
    "data": [
        {
            "input_filepath": "",
            "scale": 0,
            "output_filename": ""
        }
    ]
}
```

## version 3

- `"scaler"`: convert and resize image(s) each with a scale value
    - arg:
        - `--data`: a JSON object

in this future version, the added options are:
- `output_file_format (optional)`:
    - the format of the scaled image
    - if not given, will be format of input image file

json format:
```json
{
    "data": [
        {
            "input_filepath": "",
            "scale": 0,
            "output_filename": "",
            "output_file_format": ""
        }
    ]
}
```

# deployment

Imagine we are to turn the script in Section A into a cloud service. You can assume that the
original script has been expanded into a feature-complete wrapper for ImageMagick. Describe
how you would scale this into a service that is capable of handling thousands of requests per
minute.

In your answer you should consider the following:
- Infrastructure: which hosting platform and specific services would you use (feel free to
draw any diagrams to aid in the description of your architecture choices)?
- Implementation: deployment pipeline, testing, on-going service maintenance, availability
and redundancy.
- Observability: logging, monitoring and alarming.
- Variable load: how would you design the service for spiky / smooth / constant demand?
- Data persistence: how would you persist results and image metadata?
