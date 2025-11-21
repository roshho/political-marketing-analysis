from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

# Manually constructing y_true and y_pred from the confusion matrix
y_true = []
y_pred = []

# Predicted 0
y_true.extend([0] * 283)  # 283 times predicted 0 actual 0
y_pred.extend([0] * 283)

y_true.extend([1] * 3)    # 3 times predicted 0 actual 1
y_pred.extend([0] * 3)

y_true.extend([2] * 287)  # 287 times predicted 0 actual 2
y_pred.extend([0] * 287)

# Predicted 1
y_true.extend([0] * 10)   # 10 times predicted 1 actual 0
y_pred.extend([1] * 10)

y_true.extend([1] * 5)    # 5 times predicted 1 actual 1
y_pred.extend([1] * 5)

y_true.extend([2] * 18)   # 18 times predicted 1 actual 2
y_pred.extend([1] * 18)

# Predicted 2
y_true.extend([0] * 15)   # 15 times predicted 2 actual 0
y_pred.extend([2] * 15)

y_true.extend([1] * 1)    # 1 time predicted 2 actual 1
y_pred.extend([2] * 1)

y_true.extend([2] * 160)  # 160 times predicted 2 actual 2
y_pred.extend([2] * 160) 

# Compute precision, recall, and F1 score
precision = precision_score(y_true, y_pred, average=None)
recall = recall_score(y_true, y_pred, average=None)
f1 = f1_score(y_true, y_pred, average=None)

print("Precision per class:", precision)
print("Recall per class:", recall)
print("F1 Score per class:", f1)

# Macro and Micro averaged Precision, Recall, and F1 Score
macro_precision = precision_score(y_true, y_pred, average='macro')
macro_recall = recall_score(y_true, y_pred, average='macro')
macro_f1 = f1_score(y_true, y_pred, average='macro')

micro_precision = precision_score(y_true, y_pred, average='micro')
micro_recall = recall_score(y_true, y_pred, average='micro')
micro_f1 = f1_score(y_true, y_pred, average='micro')

print("Macro Precision:", macro_precision)
print("Macro Recall:", macro_recall)
print("Macro F1 Score:", macro_f1)
print("Micro Precision:", micro_precision)
print("Micro Recall:", micro_recall)
print("Micro F1 Score:", micro_f1)

# Compute accuracy
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)
