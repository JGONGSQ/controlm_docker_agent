import getopt
import sys


def main(argv):
    kJobname = ''
    kNameSpace = None
    kYaml = ''
    kVname = []
    kVvalue = []
    kImagename = 'none'
    kpvolclaim = 'none'
    kimagepullpolicy = 'Always'
    kimagepullsecret = 'regcred'
    krestartpolicy = 'Never'
    kbackofflimit = 0
    khostpath = 'none'
    kvolname = 'none'
    kvolpath = 'none'
    kcommands = []
    kargs = []

    # Arguments:
    #   a|args              arguments to pass to -k|Commands (default is None)
    #   b|backofflimit      default is 0
    #   c|claim             PersistentVolumeClaim
    #   e|envname           environment variable name
    #   H|hostpath          Path on host machine (must be a directory}
    #   i|image             container image name
    #   j|jobname           Mandatory. Job name
    #   m|volname           Volume mount name
    #   m|commands          Commands to run in container (entrypoint)
    #   p|image_pull_policy Always or Latest
    #   r|restartpolicy     default is Never
    #   s|imagesecret       name of image_pull_secret
    #   t|volpath           Volume mount path in Pod
    #   v|envvalue          variable value
    #   y|yaml              name of a yaml manifest for job creation. Overrides all others except jobname
    #
    try:
        opts, args = getopt.getopt(argv, "hj:c:i:e:v:y:p:s:r:b:H:m:t:a:k:",
                                   ["jobname=", "claim=", "image=", "envname=", "envvalue=", "yaml=",
                                    "imagepullpolicy=",
                                    "imagepullsecret=", "restartpolicy=", "backofflimit=", "hostpath=",
                                    "volname=", "volpath=", "commands=", "args="])
    except getopt.GetoptError:
        # usage()
        sys.exit(1)

    for opt, arg in opts:
        print("############################")
        print(opt, arg)

        if opt == '-h':
            # usage()
            sys.exit(0)
        elif opt in ("-e", "--envname"):
            kVname.append(arg)
        elif opt in ("-c", "--claim"):
            kpvolclaim = arg
        elif opt in ("-i", "--image"):
            kImagename = arg
        elif opt in ("-j", "--jobname"):
            kJobname = arg
        elif opt in ("-n", "--namespace"):
            kNameSpace = arg
        elif opt in ("-v", "--envvalue"):
            kVvalue.append(arg)
        elif opt in ("-y", "--yaml"):
            kYaml = arg
        elif opt in ("-b", "--backofflimit"):
            kbackofflimit = int(arg)
        elif opt in ("-p", "--imagepullpolicy"):
            kimagepullpolicy = arg
        elif opt in ("-r", "--restartpolicy"):
            krestartpolicy = arg
        elif opt in ("-s", "--imagepullsecret"):
            kimagepullsecret = arg
        elif opt in ("-H", "--hostpath"):
            khostpath = arg
        elif opt in ("-m", "--volname"):
            kvolname = arg
        elif opt in ("-k", "--commands"):
            kcommands.append(arg)
        elif opt in ("-a", "--args"):
            kargs.append(arg)


if __name__ == '__main__':
    main(sys.argv[1:])
