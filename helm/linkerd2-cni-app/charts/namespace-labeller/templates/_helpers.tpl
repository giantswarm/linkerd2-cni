{{- define "jobAnnotations" -}}
"helm.sh/hook": "pre-install"
"helm.sh/hook-delete-policy": "before-hook-creation,hook-succeeded,hook-failed"
{{- end -}}

{{- define "jobLabels" -}}
app: "{{ .Values.name }}"
giantswarm.io/service-type: "managed"
{{- end -}}
