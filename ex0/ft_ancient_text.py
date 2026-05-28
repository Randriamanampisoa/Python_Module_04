#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:55:28 by fanilran            #+#    #+#            #
#   Updated: 2026/05/28 14:49:08 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


# def verifie()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    elif len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {sys.argv[1]}")
        try:
            file = open(sys.argv[1], "r")
            print("---\n")
            print(file.read())
            print("---")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")