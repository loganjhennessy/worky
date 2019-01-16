#!/bin/bash

command=$1

case ${command} in
"create" | "delete" | "list" | "update")
    pywky ${@}
    ;;
"get")
    pywky ${@}
    ;;
*)
    pywky ${@}
    ;;
esac
