import {ReactNode} from "react";

export default function AdminLayout({children}: { children: ReactNode }) {
    return (
        <div>
            <header>Admin layout header</header>
            <div>{children}</div>
        </div>
    )
}
