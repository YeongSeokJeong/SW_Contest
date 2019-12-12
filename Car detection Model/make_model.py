from keras.layers import Input,Conv2D,MaxPool2D,GlobalAveragePooling2D,Dense,Reshape
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import adam

def define_model(): 
	inputs = Input(shape = (max_row,max_col,1,))
	cnn2d_output = Conv2D(32,7,padding = 'same',activation = 'relu')(inputs)
	cnn_pooling = MaxPool2D(pool_size = (2,2))(cnn2d_output)
	cnn2d_output_1 = Conv2D(64,7,padding = 'same',activation = 'relu')(cnn_pooling)
	cnn2d_pooling_1 = MaxPool2D(pool_size = (2,2))(cnn2d_output_1)
	cnn2d_output_2 = Conv2D(128,7,padding = 'same',activation = 'relu')(cnn2d_pooling_1)
	cnn2d_pooling_2 = MaxPool2D(pool_size = (2,2))(cnn2d_output_2)
	output = GlobalAveragePooling2D()(cnn2d_pooling_2)
	output = Dense(128,activation = 'relu')(output)
	result = Dense(2,activation = 'softmax')(output)
	model = Model(inputs,result)
	model.summary()
	model.compile(loss = "binary_crossentropy",optimizer = 'adam',metrics = ['accuracy'])
	return model