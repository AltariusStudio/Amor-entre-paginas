init python:

    ### Function to call the writing of the note in a new context.
    def write_the_note():
        global note
        note = renpy.input("what's up?",default="",screen="input_note")
        return note

    ### Log a typo to the file.
    def add_typo():
        with open( os.path.join( renpy.config.gamedir, "renedit/EditingLog.txt" ), 'a+' ) as editlog:
            editlog.write("\nTypo logged at "+ str(renpy.get_filename_line()) + ":\n" + _last_say_what + "\n\n----------------------------\n")
        editlog.close()
        issue_log_line = renpy.get_filename_line()
        persistent.issue_log.append((issue_log_line,"typo"))
        persistent.total_typo_count += 1
        renpy.notify("Successfully logged typo to file.")

    ### Add a note to the file.
    def add_note():
        global note
        global view_
        renpy.invoke_in_new_context(write_the_note)
        if note == "CLEAR DATA": ## Let the user clear data.
            renpy.call_in_new_context("confirm_deletion")
        elif note == "VIEW TOTALS": ## Let the user view totals.
            persistent.visible_log = not persistent.visible_log
        elif note == "ALLOW MULTI":
            persistent.allow_multi = not persistent.allow_multi
        elif note == "HELP":
            renpy.show_screen("renedit_help")
        elif note != "": ## Log any actual input,
            with open( os.path.join( renpy.config.gamedir, "renedit/EditingLog.txt" ), 'a+' ) as editlog:
                editlog.write( "\nNote created at " + str(renpy.get_filename_line()) +":\n"+ note + "\n\n----------------------------\n")
            editlog.close()
            renpy.notify("Successfully added note to file.")
            issue_log_line = renpy.get_filename_line()
            persistent.total_note_count += 1
            persistent.issue_log.append((issue_log_line,"note"))

        else: ## And don't log it if there's none.
            renpy.notify("Adding note cancelled.")

label confirm_deletion:

    menu:
        "Do you want to clear all editing data?"
        "Yes, delete all persistent typo/note data. (This will not effect EditingLog.txt)":
            $ persistent.issue_log = []
            $ persistent.total_typo_count = 0
            $ persistent.total_note_count = 0
            return
        "Yes, {b}and{/b} clear the Editing Log. (Deletes all content of EditingLog.txt)":
            $ persistent.issue_log = []
            $ persistent.total_typo_count = 0
            $ persistent.total_note_count = 0
            python:
                with open( os.path.join( renpy.config.gamedir, "renedit/EditingLog.txt" ), 'w' ) as editlog:
                    editlog.write("")
            return
        "No!!!":
            return
