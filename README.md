 Student Support Early Warning System

This BYOP project predicts whether a college student may need early academic support based on routine indicators such as attendance, study time, sleep, assignment submission rate, internal marks, screen time, and stress level.

The problem is practical and local to student life: many students struggle quietly until performance drops sharply. A lightweight prediction tool can help identify risk earlier so that mentors or the student can intervene sooner.

## Why this project fits Fundamentals of AI and ML

The project applies core concepts from the course:

- problem definition as a binary classification task
- feature selection from real student-life factors
- dataset preparation
- model training using logistic regression
- evaluation using accuracy, precision, recall, F1-score, and a confusion matrix
- model inference on new input data

To keep the repository easy to run in any environment, the model is implemented from scratch in pure Python rather than using external ML libraries.

## Project structure

```text
BYOP/
├── data/
│   └── student_support_dataset.csv
├── models/
│   ├── evaluation.txt
│   └── student_support_model.json
├── report/
│   └── Project_Report.md
└── src/
    ├── data_generation.py
    ├── model.py
    ├── predict.py
    └── train.py
```

## Problem statement

Students often face a combination of low attendance, poor sleep, high stress, and inconsistent coursework submission. These warning signs may not be acted on quickly enough. This project builds a simple ML-based early warning system that classifies whether a student is likely to need support.

## Dataset

The dataset used here is synthetically generated but based on realistic academic and lifestyle indicators. This approach keeps the project self-contained and avoids privacy issues around personal student records.

Features:

- `attendance_pct`
- `study_hours_per_day`
- `sleep_hours`
- `assignments_submitted_pct`
- `internal_score`
- `screen_time_hours`
- `stress_level`

Target:

- `support_needed`

## How to run

Generate the dataset, train the model, and evaluate it:

```bash
python3 src/train.py
```

Run a sample prediction:

```bash
python3 src/predict.py \
  --attendance 58 \
  --study-hours 1.5 \
  --sleep-hours 5.2 \
  --assignment-pct 60 \
  --internal-score 55 \
  --screen-time 7 \
  --stress-level 8
```

## Sample output

After training, the project creates:

- `data/student_support_dataset.csv`
- `models/student_support_model.json`
- `models/evaluation.txt`

The prediction command returns:

- class label
- risk probability
- decision threshold

## Key design choices

- Chose a student-centered problem relevant to campus life.
- Used logistic regression because it is interpretable and well-suited for binary classification.
- Implemented the algorithm manually to demonstrate understanding of the learning process.
- Used a synthetic dataset to stay privacy-safe and reproducible.

## Limitations

- The dataset is simulated, so performance does not represent real deployment quality.
- The model is intended for educational demonstration, not for high-stakes academic decisions.
- Real-world deployment would require ethically collected student data, consent, bias checks, and faculty validation.

## Future improvements

- collect anonymized real student data with permission
- compare logistic regression with decision trees or k-nearest neighbors
- add a simple web interface
- visualize feature impact and model confidence

## Submission checklist

- GitHub-ready repository with meaningful structure
- Detailed report in Repository as Project Report
- Clear README for setup and usage
