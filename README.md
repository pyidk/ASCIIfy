# ASCIIfy

This is a small project which the program takes an image as an input and converts it into ASCII art.

![Mona Lisa](./examples/mona-lisa_ascii.png)

## Usage

This project depends on two Python packages -- NumPy and PIL. These packages can be installed by running the following command in a clone of this repository:

```bash
python -m pip install -r requirements.txt
```

After the installation is complete, you can use this project to convert an image into ASCII art. In order to do so, simply write the following bit of code:

```python
from asciify import ASCIIfy

image = ASCIIfy("path/to/image.png", path_to_font="path/to/font.ttf", font_size=10)
image.show()  # To directly show image
# or
image.save("path/to/file.png", format='PNG')  # to save image to a specific directory
```

## Contributing

Contributions are welcome! Here's what you can do to help:

### Reporting Bugs
1. Check the issue tracker to see if your issue has already been reported.
2. If not, create a new issue describing the bug, providing as much detail as you can.

### Suggesting Enhancements
1. Check the issue tracker to see if your suggestion has already been made.
2. If not, create a new issue, describing your suggestion in detail.

#### Pull Requests
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your changes to your fork
5. Submit a pull request

## License

This project is under the MIT License, so you are free to use or refer to this project whenever you need. See the [LICENSE](./LICENSE) of this project for more details.
