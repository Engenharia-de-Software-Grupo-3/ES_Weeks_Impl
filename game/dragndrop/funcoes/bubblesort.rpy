init python:

    def setup_python_bs_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(5):
            start_x = 530
            start_y = 700
            end_x = 1580
            end_y = 950
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_python_bs.append(rand_loc) # Add the random locations to a list so we can use them
    
    def setup_java_bs_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(7):
            start_x = 530
            start_y = 700
            end_x = 1580
            end_y = 950
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_java_bs.append(rand_loc) # Add the random locations to a list so we can use them

    def setup_ruby_bs_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(5):
            start_x = 530
            start_y = 700
            end_x = 1580
            end_y = 950
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_ruby_bs.append(rand_loc) # Add the random locations to a list so we can use them
    
    def setup_lua_bs_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(5):
            start_x = 530
            start_y = 700
            end_x = 1580
            end_y = 950
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_lua_bs.append(rand_loc) # Add the random locations to a list so we can use them

    def piece_drop_python_bs (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_python_bs
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_python_bs += 1
            if finished_pieces_python_bs == page_pieces_python_bs:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("python_bs_complete")
    
    def piece_drop_java_bs (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_java_bs
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_java_bs += 1
            if finished_pieces_java_bs == page_pieces_java_bs:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("java_bs_complete")
    
    def piece_drop_ruby_bs (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_ruby_bs
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_ruby_bs += 1
            if finished_pieces_ruby_bs == page_pieces_ruby_bs:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("ruby_bs_complete")
    
    def piece_drop_lua_bs (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_lua_bs
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_lua_bs += 1
            if finished_pieces_lua_bs == page_pieces_lua_bs:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("lua_bs_complete")