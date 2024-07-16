####################
### oral-written ###
####################

### verbs
python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_1000.conllu \
--output ../results/oral_written_verbs_1000sent_md2_an100.json \
--patterns ../patterns_oral_written_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2000.conllu \
--output ../results/oral_written_verbs_2000sent_md2_an100.json \
--patterns ../patterns_oral_written_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2776.conllu \
--output ../results/oral_written_verbs_2776sent_md2_an100.json \
--patterns ../patterns_oral_written_verbs.yml \
--max-degree 2 \
--alpha-num 100

## nouns
python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_1000.conllu \
--output ../results/oral_written_nouns_1000sent_md2_an100.json \
--patterns ../patterns_oral_written_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2000.conllu \
--output ../results/oral_written_nouns_2000sent_md2_an100.json \
--patterns ../patterns_oral_written_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2776.conllu \
--output ../results/oral_written_nouns_2776sent_md2_an100.json \
--patterns ../patterns_oral_written_nouns.yml \
--max-degree 2 \
--alpha-num 100

## all nodes
python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_1000.conllu \
--output ../results/oral_written_allnodes_1000sent_md2_an100.json \
--patterns ../patterns_oral_written_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2000.conllu \
--output ../results/oral_written_allnodes_2000sent_md2_an100.json \
--patterns ../patterns_oral_written_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_French-ParisStories-master_2776.conllu \
--output ../results/oral_written_allnodes_2776sent_md2_an100.json \
--patterns ../patterns_oral_written_allnodes.yml \
--max-degree 2 \
--alpha-num 100

#####################
## romanian-french ##
#####################

### verbs
python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_french_verbs_1000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_french_verbs_2000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_french_verbs_3000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

### nouns
python extract_rules.py \
 ../data/UD_French-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_french_nouns_1000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_french_nouns_2000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_french_nouns_3000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

### all nodes
python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_french_allnodes_1000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_french_allnodes_2000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_French-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_french_allnodes_3000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100

######################
## romanian-spanish ##
######################

### verbs
python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_spanish_verbs_1000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_spanish_verbs_2000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_spanish_verbs_3000sent_md2_an100.json \
--patterns ../patterns_ro_verbs.yml \
--max-degree 2 \
--alpha-num 100

### nouns
python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_spanish_nouns_1000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_spanish_nouns_2000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_spanish_nouns_3000sent_md2_an100.json \
--patterns ../patterns_ro_nouns.yml \
--max-degree 2 \
--alpha-num 100

### all nodes
python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_1000.conllu \
--output ../results/romanian_spanish_allnodes_1000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_2000.conllu \
--output ../results/romanian_spanish_allnodes_2000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100

python extract_rules.py \
../data/UD_Spanish-GSD-master_UD_Romanian-RRT-master_3000.conllu \
--output ../results/romanian_spanish_allnodes_3000sent_md2_an100.json \
--patterns ../patterns_ro_allnodes.yml \
--max-degree 2 \
--alpha-num 100