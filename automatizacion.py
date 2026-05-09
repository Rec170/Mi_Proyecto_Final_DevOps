#!/usr/bin/env python3

import boto3
from datetime import datetime, timedelta


def listar_instancias_ec2():
    print("\n========== INSTANCIAS EC2 ==========")
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    found = False
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            found = True
            print(f"ID: {instance['InstanceId']}")
            print(f"Tipo: {instance['InstanceType']}")
            print(f"Estado: {instance['State']['Name']}")
            print("-" * 40)

    if not found:
        print("No se encontraron instancias EC2.")


def reporte_cpu_ec2():
    print("\n========== REPORTE CPU (24 HORAS) ==========")

    ec2 = boto3.client("ec2")
    cloudwatch = boto3.client("cloudwatch")

    response = ec2.describe_instances()

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)

    found = False

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] != "running":
                continue

            found = True
            instance_id = instance["InstanceId"]

            metrics = cloudwatch.get_metric_statistics(
                Namespace="AWS/EC2",
                MetricName="CPUUtilization",
                Dimensions=[
                    {
                        "Name": "InstanceId",
                        "Value": instance_id
                    }
                ],
                StartTime=start_time,
                EndTime=end_time,
                Period=3600,
                Statistics=["Average"]
            )

            datapoints = metrics["Datapoints"]

            if datapoints:
                promedio = sum(d["Average"] for d in datapoints) / len(datapoints)
                print(f"Instancia: {instance_id}")
                print(f"CPU Promedio (24h): {promedio:.2f}%")
            else:
                print(f"Instancia: {instance_id}")
                print("Sin métricas disponibles.")

            print("-" * 40)

    if not found:
        print("No hay instancias EC2 en ejecución.")


def listar_buckets_s3():
    print("\n========== BUCKETS S3 ==========")

    s3 = boto3.client("s3")
    response = s3.list_buckets()

    buckets = response.get("Buckets", [])

    if not buckets:
        print("No se encontraron buckets.")
        return

    for bucket in buckets:
        bucket_name = bucket["Name"]
        print(f"Bucket: {bucket_name}")

        objects = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" in objects:
            for obj in objects["Contents"]:
                print(f"  - {obj['Key']}")
        else:
            print("  (Sin objetos)")

        print("-" * 40)


def listar_autoscaling_groups():
    print("\n========== AUTO SCALING GROUPS ==========")

    autoscaling = boto3.client("autoscaling")
    response = autoscaling.describe_auto_scaling_groups()

    groups = response.get("AutoScalingGroups", [])

    if not groups:
        print("No se encontraron grupos de Auto Scaling.")
        return

    for group in groups:
        print(f"Nombre: {group['AutoScalingGroupName']}")
        print(f"Capacidad mínima: {group['MinSize']}")
        print(f"Capacidad máxima: {group['MaxSize']}")
        print(f"Capacidad deseada: {group['DesiredCapacity']}")
        print("-" * 40)


def main():
    listar_instancias_ec2()
    reporte_cpu_ec2()
    listar_buckets_s3()
    listar_autoscaling_groups()


if __name__ == "__main__":
    main()
