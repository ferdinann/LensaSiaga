# 🤝 Contributing to LensaSiaga

Thank you for your interest in contributing to LensaSiaga! This document provides guidelines for contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Expected Behavior

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers and help them learn
- ✅ Focus on what is best for the community
- ✅ Show empathy towards other community members

### Unacceptable Behavior

- ❌ Harassment, discrimination, or offensive comments
- ❌ Trolling, insulting/derogatory comments
- ❌ Public or private harassment
- ❌ Publishing others' private information

---

## 🛠️ How Can I Contribute?

### 1. Reporting Bugs 🐛

**Before Submitting**:
- Check existing issues to avoid duplicates
- Verify the bug in the latest version
- Collect relevant information

**Bug Report Should Include**:
```markdown
**Description**: Clear description of the bug

**Steps to Reproduce**:
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Screenshots**: If applicable

**Environment**:
- OS: [e.g., Windows 11]
- Python Version: [e.g., 3.11]
- LensaSiaga Version: [e.g., 1.0.0]
- Browser: [e.g., Chrome 120]

**Additional Context**: Any other relevant information
```

### 2. Suggesting Features 💡

**Feature Request Should Include**:
```markdown
**Feature Description**: Clear description

**Problem it Solves**: What problem does this solve?

**Proposed Solution**: How should it work?

**Alternatives Considered**: Other solutions you've thought about

**Additional Context**: Screenshots, mockups, examples
```

### 3. Contributing Code 💻

#### Types of Contributions

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance improvements
- ✅ Tests
- 🌐 Translations

---

## 🔧 Development Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual environment (recommended)

### Setup Steps

1. **Fork the Repository**
```bash
# Click 'Fork' on GitHub
```

2. **Clone Your Fork**
```bash
git clone https://github.com/YOUR_USERNAME/lensasiaga.git
cd lensasiaga
```

3. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available
```

5. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

6. **Make Your Changes**
```bash
# Code away! 🚀
```

7. **Test Your Changes**
```bash
streamlit run app.py
# Test thoroughly
```

8. **Commit Your Changes**
```bash
git add .
git commit -m "feat: add amazing feature"
```

9. **Push to Your Fork**
```bash
git push origin feature/your-feature-name
```

10. **Create Pull Request**
```bash
# Go to GitHub and click 'New Pull Request'
```

---

## 📏 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) guidelines:

```python
# Good ✅
def calculate_confidence_score(predictions):
    """Calculate confidence score from predictions."""
    return float(np.max(predictions)) * 100

# Bad ❌
def calc(p):
    return float(np.max(p))*100
```

### Code Organization

```python
# File structure
"""
Module docstring explaining purpose.
"""

# Imports (standard library, third-party, local)
import os
import numpy as np
from local_module import function

# Constants
MAX_UPLOAD_SIZE = 200

# Classes
class ImageProcessor:
    """Class docstring."""
    pass

# Functions
def process_image(image):
    """Function docstring."""
    pass

# Main execution
if __name__ == "__main__":
    main()
```

### Naming Conventions

```python
# Variables & Functions: snake_case
user_name = "John"
def get_predictions():
    pass

# Classes: PascalCase
class ImageClassifier:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_PREDICTIONS = 5
DEFAULT_LOCATION = (3.5952, 98.6722)

# Private: _leading_underscore
def _internal_function():
    pass
```

### Documentation

```python
def predict_image(model, image, class_names):
    """
    Predict the class of an image using the model.
    
    Args:
        model: TensorFlow model for prediction
        image: PIL Image object
        class_names: List of class names
        
    Returns:
        tuple: (predicted_class, confidence, all_predictions)
        
    Raises:
        ValueError: If image is invalid
        
    Example:
        >>> img = Image.open("test.jpg")
        >>> pred, conf, all_pred = predict_image(model, img, classes)
        >>> print(f"Predicted: {pred} ({conf:.2f}%)")
    """
    # Implementation
    pass
```

---

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Adding/updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good ✅
feat(ui): add dark mode toggle
fix(model): correct preprocessing normalization
docs(readme): update installation instructions
style(app): format code with black
refactor(detection): simplify prediction logic
perf(cache): optimize model loading
test(utils): add unit tests for preprocessing
chore(deps): update tensorflow to 2.15.0

# Bad ❌
update stuff
fixed bug
changes
```

### Commit Message Body

```
feat(gps): add coordinate validation

- Validate latitude range (-90 to 90)
- Validate longitude range (-180 to 180)
- Display error message for invalid coordinates
- Add unit tests for validation logic

Closes #123
```

---

## 🔄 Pull Request Process

### Before Submitting

- ✅ Test your changes thoroughly
- ✅ Update documentation if needed
- ✅ Add/update tests if applicable
- ✅ Follow coding standards
- ✅ Rebase on latest main branch
- ✅ Ensure no merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing done:
- [ ] Manual testing
- [ ] Unit tests added/updated
- [ ] Integration tests passed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally

## Screenshots (if applicable)
Add screenshots here

## Related Issues
Closes #(issue number)
```

### Review Process

1. **Automated Checks**: CI/CD will run tests
2. **Code Review**: Maintainers will review
3. **Feedback**: Address review comments
4. **Approval**: At least 1 approval required
5. **Merge**: Maintainer will merge

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_preprocessing.py

# Run with coverage
pytest --cov=app tests/
```

### Writing Tests

```python
import pytest
from app import preprocess_image

def test_preprocess_image():
    """Test image preprocessing."""
    # Arrange
    image = create_test_image()
    
    # Act
    result = preprocess_image(image)
    
    # Assert
    assert result.shape == (1, 224, 224, 3)
    assert result.min() >= 0
    assert result.max() <= 1
```

---

## 📚 Documentation

### Code Comments

```python
# Good ✅
# Calculate confidence score as percentage
confidence = float(predictions[0][predicted_class_idx]) * 100

# Bad ❌
# calc conf
confidence = float(predictions[0][predicted_class_idx]) * 100
```

### Docstrings

Use Google-style docstrings:

```python
def load_model(model_path):
    """
    Load TensorFlow model from file.
    
    Args:
        model_path (str): Path to the .h5 model file
        
    Returns:
        tf.keras.Model: Loaded Keras model
        
    Raises:
        FileNotFoundError: If model file doesn't exist
        ValueError: If model file is corrupted
    """
    pass
```

---

## 🎨 UI/UX Contributions

### Design Guidelines

- Maintain dark theme consistency
- Use established color palette
- Ensure mobile responsiveness
- Test on multiple browsers
- Follow accessibility guidelines (WCAG)
- Add appropriate animations

### CSS Best Practices

```css
/* Good ✅ */
.card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 1.5rem;
    transition: transform 0.3s ease;
}

/* Bad ❌ */
.card{background:#fff;padding:10px}
```

---

## 🌐 Internationalization (i18n)

When adding translations:

```python
# Use translation keys
TRANSLATIONS = {
    "en": {
        "upload_image": "Upload Image",
        "analyze_button": "Analyze Image"
    },
    "id": {
        "upload_image": "Unggah Gambar",
        "analyze_button": "Analisis Gambar"
    }
}
```

---

## 📊 Performance Guidelines

- Optimize model loading with caching
- Minimize re-renders in Streamlit
- Use efficient data structures
- Lazy load heavy resources
- Profile code for bottlenecks

```python
# Good ✅ - Use caching
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model.h5")

# Bad ❌ - No caching
def load_model():
    return tf.keras.models.load_model("model.h5")
```

---

## 🔒 Security Guidelines

- Never commit sensitive data
- Use environment variables for secrets
- Validate all user inputs
- Sanitize file uploads
- Follow OWASP guidelines

```python
# Good ✅
allowed_extensions = {'.png', '.jpg', '.jpeg'}
if file.suffix.lower() not in allowed_extensions:
    raise ValueError("Invalid file type")

# Bad ❌
# Accept any file without validation
```

---

## 📞 Getting Help

- **Discord**: Join our community server
- **Email**: dev@lensasiaga.id
- **GitHub Discussions**: Ask questions
- **Stack Overflow**: Tag with `lensasiaga`

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Given credit in documentation
- Invited to join core team (for regular contributors)

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Your contributions make LensaSiaga better for everyone! 

Every contribution, no matter how small, is valued and appreciated. 

**Together, we're building a safer future! 🚨**

---

*For questions about contributing, contact: dev@lensasiaga.id*
