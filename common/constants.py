from readingconfig import vip, port, repo

NEXUS_HOST = "http://{vip}:{port}".format(vip=vip, port=port)

NEXUS_BASE_URL = "/service/rest"
NEXUS_COMPONENTS_URL = NEXUS_HOST + NEXUS_BASE_URL + "/v1/components" + "?repository=" + repo