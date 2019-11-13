for i in $(seq -w 2 90);
do wget -c https://csr.lanl.gov/data-fence/1573636132/ZhvWw6Qvs6-nTpH7z1UQHJx3fzw=/unified-host-network-dataset-2017/netflow/netflow_day-$i.bz2;
bzip2 -dk netflow_day-0$i.bz2;
done


python3 tranlasteNetworkData.py


