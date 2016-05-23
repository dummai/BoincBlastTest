hostname > out2
echo %date%-%time% >> out2
blastn.exe -task blastn -query in.fa -db db.ref -out out -outfmt 7 -dust no -culling_limit 20
echo %date%-%time% >> out2
