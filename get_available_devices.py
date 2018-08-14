import subprocess

num_devices = int(subprocess.check_output(["./build/query_devices"]))

available_devices = []
for i in range(num_devices):
    try:
        if "NVIDIA" in subprocess.check_output(["./build/test_device",  str(i)]):
            available_devices.append(i)
    except subprocess.CalledProcessError as e:
        print(e)


print(available_devices)