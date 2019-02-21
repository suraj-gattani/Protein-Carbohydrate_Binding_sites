# coding: utf-8
# Author: Avdesh Mishra
# Code for stacking of various methods using 3-fold CV

import numpy as np
import pandas as pd
import pickle as pk
import math
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, precision_score, confusion_matrix, recall_score, f1_score, auc, matthews_corrcoef


def main():
	# read the training data file for window size 11
	features_file = pd.read_csv('feature_file_train_ws5.csv', header=None)
	features_matrix = features_file.as_matrix()
	print(features_file.shape)
	
	#print(features_matrix)
	#y = features_matrix[:,0]
	#x = features_matrix[:,1:]
	
	etc_prob = pd.read_csv('LOG_train.txt', header=None)
	etc_matrix = etc_prob.as_matrix()
			
	rdf_prob = pd.read_csv('SVM_train.txt', header=None)
	rdf_matrix = rdf_prob.as_matrix()
	print(rdf_prob.shape)
	
	knn_prob = pd.read_csv('ETC_train.txt', header=None)
	knn_matrix = knn_prob.as_matrix()
	print(knn_prob.shape)
			
	gbc_prob = pd.read_csv('XGB_train.txt', header=None)
	gbc_matrix = gbc_prob.as_matrix()
	print(gbc_prob.shape)
	
	# kgr = np.concatenate([features_matrix, knn_matrix, gbc_matrix, rdf_matrix], axis=1)
	# egr = np.concatenate([features_matrix, etc_matrix, gbc_matrix, rdf_matrix], axis=1)
	ekr = np.concatenate([features_matrix, etc_matrix, knn_matrix, rdf_matrix ,gbc_matrix], axis=1)
	# ekg = np.concatenate([features_matrix, etc_matrix, knn_matrix, gbc_matrix], axis=1)
	
	np.savetxt('Model_XGB_3_stacking_train_SVM_meta.csv', ekr, delimiter=',', fmt='%s')
	# np.savetxt('comb_features_egr_hpinws11.txt', egr, delimiter=',')
	# np.savetxt('comb_features_ekr_hpinws11.txt', ekr, delimiter=',')
	# np.savetxt('comb_features_ekg_hpinws11.txt', ekg, delimiter=',')
	
	
if __name__ == '__main__':
    main()







