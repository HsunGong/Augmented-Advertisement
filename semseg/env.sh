array=(banana date)
flag=false
for host in ${array[@]}; do
    if [ $host == `hostname` ]; then
        flag=true
        break
    fi
done

echo "Load Env in $(hostname):$(pwd)"
if [ $flag = false ]; then
    module load openmpi/4.0.0
    module load gcc cuda/10.0 cudnn/7.6.1-cuda10.0
    source activate torch10
else
    source activate base
fi



# ----------------------------------
# Colors
# ----------------------------------
BLANK='\033[0m'
GREEN='\033[1;32m' # BOLD
BLUE='\033[1;34m'
RED='\033[0;31m'
ORANGE='\033[0;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'