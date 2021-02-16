echo "HERE WE GO\n"

case "$MODE" in
"TEST")
    echo "TEST MODE!"
    ;;
"PROD")
    echo "PROD MODE!"
    uvicorn main:app --reload
    ;;
"DEV")
    echo "DEV MODE!"
    uvicorn main:app --reload
    ;;
"CELERY")
    echo "CELERY MODE!"
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
