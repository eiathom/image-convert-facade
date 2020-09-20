# using

since this library _uses_ `imagemagick` under the hood, the binary (executable)
program needs to be installed to use this library,
see [here](https://www.imagemagick.org/script/download.php).

alternatively, a Docker file has been created to use this library containerized
(thereby not affecting the host OS, or need to install a binary on the host).

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
        - delegates tasks (to downstream)
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

each layer is __dependent__ on the previous layer, and cannot (nor should not)
_communicate_ upstream (to the previous layer).

# domain model

value extracted:
- image(s) scaled

## domain

"image scaling"

- image-io
- image-resizer

## model

processes which - combine to - extract value

### image-io

eventually, with more features to be added/wrapped, this model may have its own
domain (to serve other domains including this one).

processes:
- does the image exist (the input file)
- is the image valid (the output file; can it be written to)

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
            - the image will be located under the same path as the original image

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