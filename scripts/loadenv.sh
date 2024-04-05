
echo "Loading azd .env file from current environment"
#read .env file and export all variables
#https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-pair-values

# Check if .env file exists
if [ ! -f .env ]; then
echo "No .env file found"
exit 1
fi

# Remove all existing variables
unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)

# Read .env file and export all variables
while IFS='=' read -r key value; do
    value=$(echo "$value" | sed 's/^"//' | sed 's/"$//')
    if [ -z "$value" ] 
    then
        continue
    fi
 
    # Remove leading/trailing whitespaces
    key=$(echo "$key" | sed 's/^ *//' | sed 's/ *$//')
    
    echo "$key = $value"
    export "$key=$value"
done < .env


echo 'Creating Python virtual environment ".venv" in root'
python3 -m venv .venv

echo 'Installing dependencies from "requirements.txt" into virtual environment'
./.venv/bin/python -m pip install -r requirements-dev.txt
