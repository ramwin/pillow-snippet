# pillow_snippet
some useful snippet and utils using pillow to handle image

# Requirements
* Pillow

# Install
```
pip install pillow-snippet
```

# Documentation
## Tutorial
* convert an Image to a circled Image
```
from pillow_snippet import convert
image = open("example.jpg")
image.resize((120, 120))
circled_image = convert.circle_image(image)
circled_image.save("circled_image.png")
```

# Contribution
1. clone the code
2. make your commit
3. make test
```
sudo pip install .
python3 tests/test.py
```
4. create a pull request
