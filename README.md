# Simplified 2-Point Move Command in Rhino3D

Enhance your Rhino3D workflow with a custom script that streamlines the traditional Move command by allowing a more intuitive two-point selection method. This script is designed to improve precision and speed, especially when working with heavy models.

## What is the 2-Point Move?

The **2-Point Move** command lets you move objects by specifying two points directly in the viewport:

- **Base Point**: The starting point from which the move originates.
- **Target Point**: The destination point where you want the objects to be moved.

This method mimics the natural way we think about moving objects in physical space—by picking them up from one spot and placing them in another.

## The Problem with the Traditional Move Command

When using Rhino's standard Move command on heavy models, you might notice a significant slowdown. This is because the command provides a real-time preview of the selected objects following your cursor as you specify the target point.

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` in the command line.
2. Browse to the location where you saved the script and select it.

### Method 1 Creating a Button or Alias for Easy Access (Optional)

If you plan to use this script frequently, you can create a button or an alias for quick access.

#### Creating a Toolbar Button

1. **Right-click** on an empty area of the toolbar and select **New Button**.
2. In the **Button Editor**:

   - **Left Button Command**:
     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\2pt_move.py"
     ```
     Replace `FullPathToYourScript` with the actual file path where you saved the script.
   - **Tooltip and Help**: Add a description for the button's functionality.
   - **Set an Icon (Optional)**: You can assign an icon to the button for easier identification.

#### Creating an Alias

1. Go to **Tools > Options** and select the **Aliases** tab.
2. **Create a New Alias**:

   - **Alias**: Choose a short command name, e.g., `m2`.
   - **Command Macro**:
     ```plaintext
     _-RunPythonScript "FullPathToYourScript\2pt_move.py"
     ```
     Again, replace `FullPathToYourScript` with the actual path.

3. **Use the Alias**: Type the alias (e.g., `m2`) into the command line and press **Enter** to run the script.


### Using the Command

1. **Select** the objects you want to move.
2. When prompted, **click** to specify the **Base Point**.
3. **Click** again to specify the **Target Point**.
4. The selected objects will move from the base point to the target point.

