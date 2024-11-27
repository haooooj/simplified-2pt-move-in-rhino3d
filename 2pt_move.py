import rhinoscriptsyntax as rs

def move_objects_from_point1_to_point2():
    # Step 1: Select objects to move
    objs = rs.GetObjects("Select objects to move", preselect=True)
    if not objs:
        return

    # Step 2: Select point 1
    point1 = rs.GetPoint("Select the base point (point 1)")
    if not point1:
        return

    # Step 3: Select point 2
    point2 = rs.GetPoint("Select the target point (point 2)")
    if not point2:
        return

    # Calculate the translation vector
    translation_vector = rs.VectorCreate(point2, point1)

    # Move the objects
    rs.MoveObjects(objs, translation_vector)

if __name__ == "__main__":
    move_objects_from_point1_to_point2()
