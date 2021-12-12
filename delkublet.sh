app=$1

kubectl delete deployment $app
kubectl delete svc $app
