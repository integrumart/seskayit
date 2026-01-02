# Icon Information

## Adding an Icon to the Application

To add a custom icon to the application:

1. Create or obtain an `.ico` file (Windows icon format)
2. Save it as `icon.ico` in the project root directory
3. Update `setup.py` to reference the icon:

```python
Executable(
    "seskayit.py",
    base=base,
    target_name="SesKayitEdici.exe",
    icon="icon.ico"  # Change from None to "icon.ico"
)
```

## Creating an Icon

You can create an icon using online tools:
- https://convertio.co/png-ico/ (Convert PNG to ICO)
- https://www.favicon-generator.org/ (Generate icons)

Recommended icon size: 256x256 pixels

## Free Icon Resources

- https://icons8.com/
- https://www.flaticon.com/
- https://www.iconfinder.com/

Search for: microphone, audio, recording, sound icons
