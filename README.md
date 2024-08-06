<div align="center">

<img src="https://socialify.git.ci/deepanshu414/SearchMaster/image?description=1&descriptionEditable=SearchMaster%20is%20a%20Python%20library%20that%20helps%20you%20search%20for%20files%20with%20a%20specified%20name%20across%20all%20available%20drives%20on%20your%20system&font=KoHo&forks=1&issues=1&language=1&name=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto" alt="SearchMaster" width="640" height="320" />

</div>

`SearchMaster` is a Python library that helps you search for files with a specified name across all available drives on your system. Whether you're looking for a specific document, image, or any other file type, `SearchMaster` can help you locate it quickly and efficiently.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Badges](#badges)
- [About me](#about-me-)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage/Examples](#usageexamples)
- [Links](#-links)
- [Support](#support)

## Features

- **Cross-Drive Search:** Searches across all mounted drives on your system, ensuring comprehensive file discovery.
- **Efficient File Locating:** Uses optimized search algorithms to quickly locate files, even in systems with vast amounts of data.
- **User-Friendly Output:** Provides clear and concise output, listing the full paths of the located files and the total number of matches found.
- **Customizable Search Parameters:** Allows you to specify the file name or pattern you are looking for, making it versatile for different search needs.
- **Error Handling:**  Includes robust error handling to manage issues like inaccessible directories or read permissions.

## Demo

!<img width="620" alt="new" src="https://github.com/user-attachments/assets/74b916e4-58b6-4f99-bf7a-931ed260e56d">


## Badges
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)



## About Me 🚀

👋 Hi there! I'm Deepanshu, a passionate software developer with a broad range of skills in various programming languages and technologies. I thrive on solving complex problems, building efficient solutions, and continuously learning and growing in the tech world.


## Requirements

- Python 3.x
- `psutil` library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/deepanshu414/SearchMaster.git
   ```
2. **You can install SearchMaster using pip:**

   ```sh
   pip install SearchMaster

   ```

## Usage/Examples

Here's how to use the `SearchMaster` library to search for a file named `example.txt`:

```python
# Importing search functions from the SearchMaster module
from SearchMaster import searchp, searchl

def main():
    # Perform a search using the `searchp` function and print each result one by one.
    # This function is useful for immediate feedback or incremental output.
    # Replace "example.txt" with the actual search query or file name.
    searchp("example.txt")
   
    # Perform a search using the `searchl` function and obtain the results as a list.
    # This function is useful for scenarios where results need to be processed or manipulated further.
    # Replace "example.txt" with the actual search query or file name.
    results = searchl("example.txt")

    # Print the list of results returned by `searchl`.
    # This allows you to see all results at once after the search is completed.
    print(results)

# Check if the script is being run directly (not imported as a module).
# If true, execute the `main()` function to start the program.
if __name__ == "__main__":
    main()

```
## 🔗 Links
   [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepanshu414)
   [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/DeepanshuA80670)
   [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deepanshu-antil-865508263)


## Support

For support, email deepanshuantil4113@gmail.com

   
