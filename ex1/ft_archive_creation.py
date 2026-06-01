#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/29 23:04:29 by fanilran            #+#    #+#            #
#   Updated: 2026/06/01 12:48:25 by fanilran           ###   ########.fr      #
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
                print(f"Saving data to '{new_file}'")
                new_file_up = None
                try:
                    new_file_up = open(new_file, "w")
                    new_file_up.write("\n".join(new_content))
                    print(f"Data saved in file '{new_file}'.")
                finally:
                    if new_file_up:
                        new_file_up.close()
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if file:
                file.close()
