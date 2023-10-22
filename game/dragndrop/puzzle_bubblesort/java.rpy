screen java_bs_puzzle:

    image "images/DragNDrop/bubblesort/java/background.jpg"

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces_java_bs):
            drag:
                drag_name i
                pos initial_line_coordinates_java_bs[i]
                anchor (0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/DragNDrop/bubblesort/java/piece%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces_java_bs):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop_java_bs
                pos coordinate_lines_java_bs[i]
                anchor (0.5, 0.5)
                focus_mask True
                image "images/DragNDrop/bubblesort/java/piece%s.png" % (i + 1) alpha 0.0