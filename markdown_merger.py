import customtkinter as ctk
import os

""" Merges all .md files in the specified directory into a single output .md file. """

def merge_markdown_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".md"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(f"# {filename}\n\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")

    print(f"Markdown files merged into: {output_file}")

def main():
    def on_merge_click():
        user_path = path_entry.get()
        output = os.path.expanduser("~/Downloads/merged_notes.md")

        if os.path.isdir(user_path):
            merge_markdown_files(user_path, output)
            result_label.configure(text="Merge complete!", text_color="green")
        else:
            result_label.configure(text="Invalid directory path.", text_color="red")

    # GUI setup
    root = ctk.CTk()
    root.title("Markdown Merger")
    root.geometry("400x200")  

    # Instruction label
    label = ctk.CTkLabel(root, text="Enter the folder path containing .md files:")
    label.pack(pady=10)

    # Entry field for path
    path_entry = ctk.CTkEntry(root, width=350)
    path_entry.pack()

    # Merge button
    merge_button = ctk.CTkButton(root, text="Merge", command=on_merge_click)
    merge_button.pack(pady=15)

    # Result label
    result_label = ctk.CTkLabel(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()