echo "This will take a long time, are you sure? [y/n]"
read input

if [$input -eq "y"]
then
    wget -c https://csr.lanl.gov/data-fence/1573636132/ZhvWw6Qvs6-nTpH7z1UQHJx3fzw=/unified-host-network-dataset-2017/netflow/netflow_day-2.bz2;
    bzip2 -dk netflow_day-02.bz2;
    python3 tranlasteNetworkData.py
fi

