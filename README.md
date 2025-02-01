# git-hooks

![License](https://img.shields.io/badge/license-MIT-blue) ![Python Version](https://img.shields.io/badge/python-3.9%2B-blue) ![GitHub Stars](https://img.shields.io/github/stars/igor-sosnowicz/git-hooks?style=social)

**`git-hooks`** is a lightweight, user-friendly framework designed to streamline the management of Git hooks without the hassle of external dependencies. With a collection of useful hooks included right out of the box, you can enhance your Git workflow effortlessly!

## 🚀 Features

- **Minimal Dependencies**: Just Python 3.9+ and a Bash shell are required. Works seamlessly on any modern Linux distribution.
- **Simplicity at Its Best**: Set up custom hooks with just a few straightforward commands.
- **Unmatched Flexibility**: Compatible with any executable, including Bash, fish, Python scripts, and even compiled binaries.
- **Ready to Use**: Comes pre-loaded with a selection of handy hooks to get you started immediately.

## 📦 Installation

Getting started with `git-hooks` is a breeze! Follow these simple steps:

1. **Clone the Repository**:
   ```
   git clone git@github.com:igor-sosnowicz/git-hooks.git && cd git-hooks
   ```

2. **Add Your Executables**:
   Place your scripts in the `hooks` directory. We provide several useful scripts to kickstart your workflow.

3. **Install the Hooks**:
   ```
   python3 install_hooks.py
   ```

### 🎉 You're All Set!

From this point on, you can enjoy hassle-free Git hooks management. No need to reinstall after modifying the `hooks` directory or adding/removing executables!

## 🤝 Contributing

We welcome contributions! If you have suggestions, improvements, or new hooks to add, feel free to open an issue or submit a pull request.

## 🌟 Get Involved

If you find `git-hooks` useful, please give it a star on GitHub! Your support helps us grow and improve the project.
