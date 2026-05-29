#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/29 20:23:15 by fanilran            #+#    #+#            #
#   Updated: 2026/05/29 21:58:08 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    elif len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file {sys.argv[1]}")
        file = None
        try:
            file = open(sys.argv[1], "r")
            print("---\n")
            content = file.read()
            print(content)
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.")
            lines = content.split("\n")
            new_content = []
            for line in lines:
                line_change = line.strip() + "#"
                new_content.append(line_change)
            print("\nTransform data:")
            print("---\n")
            for ligne in new_content:
                print(ligne)
            print("\n---")
            new_file = input("Enter new file name (or empty): ")
            if new_file == "":
                print("Not saving data.")
            else:
                file_magic = None
                try:
                    file_magic = open(new_file, "w")
                    file_magic.write("\n".join(new_content))
                    print("Saving data to 'new_fragment.txt'")
                    print("Data saved in file '{new_file}'.")
                finally:
                    if file_magic:
                        file_magic.close()
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if file:
                file.close()
