
# NeuroGene Analytics — Data Science Modelling Strategy

## Current modelling decision
A supervised Alzheimer's disease classifier will not be trained
or presented as a valid disease-prediction model using the current
40-sample hippocampus comparison.

## Reason
Disease status is perfectly associated with accession group:
- AD samples belong to GSM1176.
- Control samples belong to GSM300.

A classifier could learn accession/cohort-related differences
instead of disease-related biological patterns.

Age restriction and sex balancing do not remove this problem.
Ordinary random train-test splitting or cross-validation would
not resolve the confounding.

## Current project approach
- Perform exploratory statistical analysis.
- Use PCA for dimensionality reduction and visualization.
- Use probe annotation and GO summaries for biological context.
- Report statistical differences as exploratory findings.
- Do not report classifier accuracy, sensitivity or specificity
  as evidence of Alzheimer's prediction.

## Future machine-learning strategy
Before supervised modelling:
1. Obtain an independent, suitable dataset with AD and control
   samples represented across comparable processing groups.
2. Inspect study, cohort, platform and batch metadata.
3. Assess expression-scale compatibility and preprocessing.
4. Keep all samples from the same individual together when
   splitting data.
5. Perform feature selection only within training folds.
6. Use a preprocessing and modelling pipeline.
7. Compare regularized logistic regression, random forest
   and support vector machine models.
8. Use nested cross-validation where sample size permits.
9. Evaluate ROC-AUC, PR-AUC, sensitivity, specificity and
   calibration, not accuracy alone.
10. Perform independent external validation.

## Scientific scope
Any future model will be a research model for exploratory
investigation, not a clinically validated diagnostic tool.
