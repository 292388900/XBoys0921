gae 部署python 应用
--

	TUTORIALDIR=~/src/proxy1201-161008/proxy_gae0317

	git clone https://github.com/Supermans1201/proxy.git $TUTORIALDIR
#
	cd $TUTORIALDIR
#
	git checkout gcloud

#
	dev_appserver.py $PWD
#
	gcloud app deploy app.yaml --project proxy1201-161008