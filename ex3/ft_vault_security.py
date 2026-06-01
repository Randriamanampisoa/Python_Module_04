#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:56:13 by fanilran            #+#    #+#            #
#   Updated: 2026/06/01 14:54:21 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(file_name: str, mode: str) -> tuple[bool, str]:
    try:
        if mode == "read":
            print("Using 'secure_archive' to read from an inaccessible file:")
            with open(file_name, "r") as f:
                content = f.read()
        elif mode == "write":
            print("Using 'secure_archive' to write previous content to a new "
                  "file:")
            with open(file_name, "w") as f:
                content = "Content successfully written to file"
                f.write(content)
    except FileNotFoundError as e:
        return (False, f"{e}")
    except PermissionError as e:
        return (False, f"{e}")
    except Exception as e:
        return (False, f"{e}")
    return (True, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    lst = [
        ("/not/existing/file", "read"), ("master", "read"),
        ("ancient_fragment.txt", "read"), ("test_write.txt", "write")
    ]
    for t_lst in lst:
        res = secure_archive(t_lst[0], t_lst[1])
        print(res)
        print()
