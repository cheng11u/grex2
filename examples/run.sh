#!/bin/bash

python3 extract_rules_via_lasso.py \
examples/fr_pud-sud-test.conllu \
--patterns examples/patterns_subject_inversion.txt \
--output examples/rules_subject_inversion.json

python3 extract_rules_via_lasso.py \
examples/fr_pud-sud-test.conllu \
--patterns examples/patterns_agreement.txt \
--output examples/rules_agreement.json \
--max-degree 2

# python3 extract_rules_via_lasso.py \
# examples/fr_pud-ud-test.conllu \
# --patterns patterns_fr-ro_constrastive_analysis.txt \
# --output rules_constrative.json

