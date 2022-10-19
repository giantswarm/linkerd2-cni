{{/* vim: set filetype=mustache: */}}
{{/*
Namespace name helper. Switch between .Values.namespace and .Release.Namespace
if .Values.installNamespace is set.
*/}}
{{- define "linkerd-cni.namespace-name" -}}
{{- .Values.installNamespace | ternary .Values.namespace .Release.Namespace -}}
{{- end -}}
