##@ Chart

MAIN_CHART=helm/linkerd2-cni-app
VENDOR_CHART_CNI=vendor/linkerd/charts/linkerd2-cni
VENDOR_CHART_PARTIALS=vendor/linkerd/charts/partials


.PHONY: update-chart helm-docs
update-chart: ## Run vendir sync
	@echo "====> $@"
	vendir sync
	mkdir -p $(MAIN_CHART)/charts
	rm -rf $(MAIN_CHART)/templates
	rm -rf $(MAIN_CHART)/charts/partials
	cp -r $(VENDOR_CHART_CNI)/templates $(MAIN_CHART)
	cp -r $(VENDOR_CHART_PARTIALS) $(MAIN_CHART)/charts/

helm-docs:
	helm-docs -u -c $(MAIN_CHART) -g $(MAIN_CHART)
