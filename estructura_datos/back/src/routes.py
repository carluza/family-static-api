from flask import Blueprint, jsonify, request
from models import FamilyStructure

family_bp = Blueprint("family", __name__)
jackson_family = FamilyStructure("Jackson")

@family_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Familia Jackson funcionando"}), 200


@family_bp.route("/members", methods=["GET"])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200


@family_bp.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@family_bp.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()
    if "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Missing fields"}), 400

    member = jackson_family.add_member(data)
    return jsonify(member), 200

@family_bp.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if success:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404
