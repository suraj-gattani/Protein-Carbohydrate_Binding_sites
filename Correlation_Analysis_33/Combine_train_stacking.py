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
	features_file = pd.read_csv('feature_file_train_ws3.csv', header=None)
	features_matrix = features_file.as_matrix()
	print(features_file.shape)
	
	#print(features_matrix)
	#y = features_matrix[:,0]
	#x = features_matrix[:,1:]
	
	etc_prob = pd.read_csv('RDF_train.txt', header=None)
	etc_matrix_1 = etc_prob.as_matrix()
	etc_matrix=etc_matrix_1[:,1:]
	print(etc_prob.shape)
	
	rdf_prob = pd.read_csv('ETC_train.txt', header=None)
	rdf_matrix_1 = rdf_prob.as_matrix()
	rdf_matrix=rdf_matrix_1[:,1:]
	print(rdf_prob.shape)
	
	knn_prob = pd.read_csv('BAG_train.txt', header=None)
	knn_matrix_1 = knn_prob.as_matrix()
	knn_matrix=knn_matrix_1[:,1:]
	print(knn_prob.shape)
			
	
	# kgr = np.concatenate([features_matrix, knn_matrix, gbc_matrix, rdf_matrix], axis=1)
	# egr = np.concatenate([features_matrix, etc_matrix, gbc_matrix, rdf_matrix], axis=1)
	ekr = np.concatenate([features_matrix, etc_matrix, knn_matrix, rdf_matrix], axis=1)
	# ekg = np.concatenate([features_matrix, etc_matrix, knn_matrix, gbc_matrix], axis=1)
	
	np.savetxt('Model_5_stacking_train_BAG_meta_single_prob.csv', ekr, delimiter=',', fmt='%s')
	# np.savetxt('comb_features_egr_hpinws11.txt', egr, delimiter=',')
	# np.savetxt('comb_features_ekr_hpinws11.txt', ekr, delimiter=',')
	# np.savetxt('comb_features_ekg_hpinws11.txt', ekg, delimiter=',')
	
	
if __name__ == '__main__':
    main()







