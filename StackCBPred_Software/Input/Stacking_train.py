import numpy as np
import pandas as pd
import pickle as pk
import math
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC

# read the training data file for window size 1
train_df_1 = pd.read_csv('feature_file_train_ws1.csv', header=None)
train_1 = train_df_1.as_matrix()
y_1 = train_1[:,0]
X_1 = train_1[:,1:]
scaler = StandardScaler()
X_scale_1 = scaler.fit_transform(X_1)

# read the testing data file for window size 1
test_df_1 = pd.read_csv('feature_file_test_ws1.csv', header=None)
test_1 = test_df_1.as_matrix()
X_test_1 = test_1[:,1:]
X_test_scale_1 = scaler.transform(X_test_1)



# read the training data file for window size 5
train_df_5 = pd.read_csv('feature_file_train_ws5.csv', header=None)
train_5 = train_df_5.as_matrix()
y_5 = train_5[:,0]
X_5 = train_5[:,1:]
scaler = StandardScaler()
X_scale_5 = scaler.fit_transform(X_5)

# read the testing data file for window size 5
test_df_5 = pd.read_csv('feature_file_test_ws5.csv', header=None)
test_5 = test_df_5.as_matrix()
X_test_5 = test_5[:,1:]
X_test_scale_5 = scaler.transform(X_test_5)



################################ First base layer-> LogisticRegression
clf = LogisticRegression()
clf.fit(X_scale_5,y_5)
modelfile = 'Model_file_train_log.model'
pk.dump(clf, open(modelfile, 'wb'))
loaded_model = pk.load(open('Model_file_train_log.model', 'rb'))
y_pred_log_prob = loaded_model.predict_proba(X_test_scale_5)
#print("logreg_predicted")

########################## Second Base layer is ExtraTree##########################################
clf = ExtraTreesClassifier(n_estimators=1000)
clf.fit(X_scale_5,y_5)
modelfile = 'Model_file_train_etc.model'
pk.dump(clf, open(modelfile, 'wb'))
loaded_model = pk.load(open('Model_file_train_etc.model', 'rb'))
y_pred_etc_prob = loaded_model.predict_proba(X_test_scale_5)
#print("etc_predicted")

########################### Third base layer ML method is knn ###############################
clf = KNeighborsClassifier(n_neighbors=7)
clf.fit(X_scale_1,y_1)
modelfile = 'Model_file_train_knn.model'
pk.dump(clf, open(modelfile, 'wb'))
loaded_model = pk.load(open('Model_file_train_knn.model', 'rb'))
y_pred_knn_prob = loaded_model.predict_proba(X_test_scale_1)
#print("knn_predicted")

#################################### Fourth base layer is BaggingClassifier ###################
clf = SVC(C=2.378414230005442, kernel='rbf', gamma=0.013139006488339289, probability=True)
clf.fit(X_scale_5,y_5)
modelfile = 'Model_file_train_svm.model'
pk.dump(clf, open(modelfile, 'wb'))
loaded_model = pk.load(open('Model_file_train_svm.model', 'rb'))
y_pred_svm_prob = loaded_model.predict_proba(X_test_scale_5)
#print("svm_predicted")

############################### Combine probabilities of base layer to the original features and run SVM ##############################
train_df = pd.read_csv('Model_9_stacking_train_SVM_meta.csv', header=None)
train = train_df.as_matrix()
y = train[:,0]
X = train[:,1:]
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_meta_test = np.column_stack([X_test_5, y_pred_log_prob, y_pred_knn_prob, y_pred_etc_prob, y_pred_svm_prob])
X_scale_test_SVM=scaler.transform(X_meta_test)

#print("output of base layer has been addded to the original features and is ready to be used in meta layer")

# ############################# Run 10-fold with best C and Gamma #################
# clf = SVC(C=grid_fine.best_params_['C'],kernel='rbf',gamma=grid_fine.best_params_['gamma'])
clf = SVC(C=0.21022410381342863,gamma=0.0011613350732448448, probability=True)
clf.fit(X,y)
modelfile = 'Model_file_train_data.model'
pk.dump(clf, open(modelfile, 'wb'))
loaded_model = pk.load(open('Model_file_train_data.model', 'rb'))
y_pred = loaded_model.predict(X_scale_test_SVM)
y_pred_prob = loaded_model.predict_proba(X_scale_test_SVM)
y_pred = np.column_stack([y_pred, y_pred_prob])
#print("Meta_layer_predicted")

out_file = open("Results_train.txt", "w")
out_file.write("Predicted	Non-binding_prob	Binding_prob")
for m in range(len(y_pred)):
	out_file.write('\n')
	for n in range(len(y_pred[m])):
		out_file.write(str(y_pred[m][n])+'\t'+'\t')
out_file.close()








