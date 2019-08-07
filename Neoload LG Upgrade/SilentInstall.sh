# Author: Wayne Ran
# Last Modified: 2018-06-26
# Purpose: Slient install Neoload Load Generators with WAN Emulation 
# Precondition: make sure you have following files in install folder:
#
# neoload_6_2_2_linux_x64.sh
# ipfw
# ipfw_mod.ko
# agent.properties
# ------------------------------------------------------------------------------
 

sudo /opt/neoload/bin/LoadGeneratorAgentService stop

sudo sh /tmp/Neoloadfile/neoload_6_2_2_linux_x64.sh -q -dir /opt/neoload622 "-Vsys.installationTypeId=Load Generator" -Vsys.component.Common\$Boolean=true "-Vsys.component.Load Generator\$Boolean=true"

sudo cp /tmp/Neoload622files/ipfw /opt/neoload622/tools/ipfw/linux/ipfw
sudo cp /tmp/Neoload622files/ipfw_mod.ko /opt/neoload622/tools/ipfw/linux/ipfw_mod.ko

sudo chmod 755 /opt/neoload622/tools/ipfw/linux/ipfw
sudo chmod 644 /opt/neoload622/tools/ipfw/linux/ipfw_mod.ko

sudo cp /tmp/Neoload622files/agent.properties /opt/neoload622/conf/agent.properties
sudo chmod 644 /opt/neoload622/conf/agent.properties

sudo unlink /opt/neoload
sudo ln -s /opt/neoload622/ /opt/neoload

sudo /opt/neoload/bin/LoadGeneratorAgentService start
