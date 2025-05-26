import customtkinter as ctk
import os

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
        
        # Get the desired filename from the entry field
        desired_filename_from_entry = file_name_entry.get().strip()

        # Determine the final filename
        if not desired_filename_from_entry:
            final_filename = "merged_notes.md"  # Default if empty
        elif not desired_filename_from_entry.lower().endswith(".md"):
            final_filename = f"{desired_filename_from_entry}.md"  # Add .md if missing
        else:
            final_filename = desired_filename_from_entry # Use as is

        # Construct the full output path in the Downloads directory
        downloads_path = os.path.expanduser("~/Downloads")
        
        # Ensure the Downloads directory exists
        if not os.path.exists(downloads_path):
            try:
                os.makedirs(downloads_path)
            except OSError as e:
                result_label.configure(text=f"Error creating Downloads dir: {e}", text_color="red")
                return

        output_file_path = os.path.join(downloads_path, final_filename)

        if os.path.isdir(user_path):
            merge_markdown_files(user_path, output_file_path)
            result_label.configure(text=f"Merge complete! Saved as '{final_filename}' in Downloads.", text_color="green")
        else:
            result_label.configure(text="Invalid directory path.", text_color="red")

    # GUI setup
    root = ctk.CTk()
    root.title("Markdown Merger")
    root.geometry("800x400")  

    # --- File Path Entry ---
    label = ctk.CTkLabel(root, text="Enter the folder path containing .md files:")
    label.pack(pady=10)

    path_entry = ctk.CTkEntry(root, width=350) 
    path_entry.pack()

    # --- File Name Entry ---
    label = ctk.CTkLabel(root, text="Enter file name:")
    label.pack(pady=(30, 10))

    file_name_entry = ctk.CTkEntry(root, width=350)
    file_name_entry.pack()

    # --- Merge Button ---
    merge_button = ctk.CTkButton(root, text="Merge", command=on_merge_click)
    merge_button.pack(pady=15)

    # --- Result Label ---
    result_label = ctk.CTkLabel(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()