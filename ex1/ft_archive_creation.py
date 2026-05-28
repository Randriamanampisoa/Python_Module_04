#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:56:20 by fanilran            #+#    #+#            #
#   Updated: 2026/05/28 14:01:56 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

with open("notes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:  # L'objet fichier est un itérable
        print(ligne.strip())