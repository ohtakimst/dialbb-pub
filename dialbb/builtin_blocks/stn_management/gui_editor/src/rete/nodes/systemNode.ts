import { ClassicPreset as Classic } from "rete";
import type { DataflowNode } from "rete-engine";
import { socket } from "../sockets";
import { CustomInputControl } from "../utils";

export class systemNode extends Classic.Node<
  { state: Classic.Socket },    // Input socket
  { next: Classic.Socket },     // Output socket
  { type: Classic.InputControl<"text">;
    status: Classic.InputControl<"text">;
    utterance: Classic.InputControl<"text"> } // コントロール
  >
  implements DataflowNode {
  width = 220;
  height = 360;
  constructor(
    // change?: (value: number) => void,
    change?: () => void,
    private update?: (control: Classic.InputControl<"text">) => void,
    type: string = "", status: string = "", sysUtter: string = ""
    ) {
    super("systemNode");
    // 状態-タイプ
    this.addControl(
      "type",
      new CustomInputControl("text", "type", { initial: type })
    );
    // 状態-名称（省略可能）
    this.addControl(
      "status",
      new CustomInputControl("text", "name", { initial: status })
    );
    // システム発話パターン
    this.addControl(
      "utterance",
      new CustomInputControl("text", "utterance", { initial: sysUtter })
    );

    // 入出力ソケットの実装
    this.addInput("state", new Classic.Input(socket, "from user", true));
    this.addOutput("next", new Classic.Output(socket, "to user", true));
  }

  // ソケット送受信のデータ処理関数
  data(inputs: { state?: string }): { next: string } {
    // Inputデータ(次状態)
    console.log("@inputs:"+inputs.state);
    return {
      next: ""
    };
  }

  serialize() {
    const leftControl = this.inputs["state"]?.control;
    const rightControl = this.inputs["state"]?.control;

    return {
      left: (leftControl as Classic.InputControl<"number">).value,
      right: (rightControl as Classic.InputControl<"number">).value
    };
  }
}
