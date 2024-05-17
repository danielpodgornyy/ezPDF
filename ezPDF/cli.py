import argparse
import pypdf
import merge

# A custom action that allows you to only take in files with a .pdf extension
class OnlyAcceptPDF(argparse.Action):
    def __call__(self, parser, namespace, values, option_string = None):
        valuesToCheck = list()

        # If values only has one argument, append it to a temporary list
        if type(values) == str:
            valuesToCheck.append(values)
        # Otherwise, set the temp list to the input list
        else:
            valuesToCheck = values

        for value in valuesToCheck:
            if value[-4::] == ".pdf":
                setattr(namespace, self.dest, values)
            else:
                # 2 for command-line syntax errors and 1 for all other errors
                parser.exit(2, "error: atleast one of the arguments is not a PDF\n")

def Main():
    # a global parser that acts as the parent program/command
    global_parser = argparse.ArgumentParser(
        prog = "ezPDF",
        description = "An simple interface to interact with pdf files in the terminal"
        )

    subparsers = global_parser.add_subparsers(
        dest = "subcommand",
        title = "subcommands",
        help = "PDF utilies",
        )

    # create merge command
    merge_parser = subparsers.add_parser(
        "merge",
        prog = "ezPDF merge",
        description = "Merge any number of PDF files together",
        help = "Merge any number of PDF files together",
        )

    merge_parser.add_argument(
        "output_file",
        help = "file where merged pdfs go",
        action = OnlyAcceptPDF
        )

    merge_parser.add_argument(
        "input_files",
        nargs = "+",
        help = "files to be merged (Atleast one)",
        action = OnlyAcceptPDF
        )


    merge_parser.set_defaults(func = merge.MergeFiles)
    args = global_parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        print("error: subcommand or option necessary")



