import boto3

def leerSQS():
	sqs = boto3.client('sqs')

	response = sqs.receive_message(
    	QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4'
	)
	
	if response == None:
		print ("No hay mensajes")
		return

	recibos = []
	ordenes= []

	for message in response["Messages"]:
		recibos.append(message["ReceiptHandle"])
		ordenes.append(message["Body"])
	return ordenes

def escribirJson(ordenes):
	archivo=open("ordenesJSON","a")
	for orden in ordenes:
		archivo.write(orden + "\n")
		print(orden)
	archivo.close()

def comenzar():
	mensajes= leerSQS()
	escribirJson(mensajes)

#for r in recibos:
   # response = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4',ReceiptHandle=r)

